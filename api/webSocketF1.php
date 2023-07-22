<?php
require 'C:\xampp\htdocs\LabRemNew\vendor\autoload.php';

// server.php

use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;
use Ratchet\Server\IoServer;
use Ratchet\Http\HttpServer;
use Ratchet\WebSocket\WsServer;

// Define a class that implements the MessageComponentInterface
class NumberUpdates implements MessageComponentInterface
{
    private $clients;
    private $number;

    public function __construct()
    {
        $this->clients = new \SplObjectStorage();
        $this->number = 0;
    }

    public function onOpen(ConnectionInterface $conn)
    {
        // Store the new connection
        $this->clients->attach($conn);
        echo "New client connected: {$conn->resourceId}\n";
        // Send the current number to the newly connected client
        $conn->send($this->number);
    }

    public function onClose(ConnectionInterface $conn)
    {
        echo "Client disconnected: {$conn->resourceId}\n";
        // Remove the connection when it is closed
        $this->clients->detach($conn);
    }

    public function onMessage(ConnectionInterface $from, $msg)
    {
        for($i=0; $i < 10 ; $i++){
            $espUrl='http://192.168.30.21';
            $url = $espUrl.'/temperature';
            $curl = curl_init();
            curl_setopt_array($curl, [
                CURLOPT_RETURNTRANSFER => 1,
                CURLOPT_URL => $url
            ]);
            $response = curl_exec($curl);
            echo $response;
            // Update the number received from the client
            $this->number = (int) $response;

            // Broadcast the updated number to all connected clients
            foreach ($this->clients as $client) {
                $client->send($this->number);
            }
        }
        
    }

    public function onError(ConnectionInterface $conn, \Exception $e)
    {
        // Handle any errors that occur
        echo "An error occurred: {$e->getMessage()}\n";
        $conn->close();
    }

}
// Set up the WebSocket server
$server = IoServer::factory(
    new HttpServer(
        new WsServer(
            new NumberUpdates
        )
    ),
    8080 // Choose the desired port number
);
$server->run();


?>
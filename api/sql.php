<?php
$data = json_decode(file_get_contents("php://input"), true);

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "labrem";
$timestamp = date('Y-m-d H:i:s');

$myfile = fopen("testfile.txt", "w");
fwrite($myfile, sizeof($data)."\n");




fclose($myfile);
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);


// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Prepare the statement
$stmt = $conn->prepare("INSERT INTO experiments (expId, tempo, x, y) VALUES (?, ?, ?, ?)");
// Bind the parameters
$stmt->bind_param("isii", $expId, $time, $x, $y);

foreach($data as $row){
  $expId=1;
  $x = $row[0];
  $y = $row[1];
  $time = $timestamp;
  $stmt->execute();   
}

// Close the connection
$stmt->close();
$conn->close();
?>
<?php

error_reporting(E_ALL);


$json=$_GET['json'];
$decoded = json_decode($_GET['json']);
$py=$decoded->py;


echo "PHP: ".$json."\n";
//echo $py;



//$cmd = "/usr/bin/python ./orbit01.py ".escapeshellarg($json);
$cmd = "/usr/bin/python ./".$py." ".escapeshellarg($json);

$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);

//var_dump($res);
echo $res;

echo 'end PHP program';



?>

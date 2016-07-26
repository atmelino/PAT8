<?php

error_reporting(E_ALL);


$json=$_GET['json'];
$decoded = json_decode($_GET['json']);
$py=$decoded->py;



$myarray['py']=$py;
$myarray['message']='';


//echo $json;
//echo "PHP: ".$json."\n";
//echo $py;



//$cmd = "/usr/bin/python ./orbit01.py ".escapeshellarg($json);
$cmd = "/usr/bin/python ./".$py." ".escapeshellarg($json);

//print $cmd;

$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);

//var_dump($res);
//echo $res;
$myarray['message'].=$res;

#echo 'end PHP program';

$encoded= json_encode($myarray);
echo $encoded;


?>

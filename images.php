<?php
session_start();
?><!doctype html public "-//W3C//DTD HTML 4.0 //EN">
<html>
<head>
       <title>Steve's PHP Rolling Daily Image List</title>
</head>
<body>
<a href="../index.html">back to main page</a><br/><br/>


<img src="rplogo.png" /><br>
This page humbly served by a Raspberry Pi
<?php

$dirname = ".";
$images = scandir($dirname);
$ignore = Array(".", "..");

$jpgOnly = glob($dir.'*.jpg');

# Table behavior ----------
$nCols = 4;
$tSize = 256;

$rowCount = 0;

echo("<table>");
foreach($jpgOnly as $curimg){
  $m = $rowCount % $nCols;

  if ($m == 0){
    if ($rowCount > 0){
        echo "</tr>";
    }
    echo "<tr>";		 
  }

  echo "<td>";		 

  # Create a mini table for each cell -----------------------
  echo("<table>");
  
  echo "<tr>";  # Image	--------------------------	 
  echo "<td>";		 
  echo "<a href='./$curimg'>";
  echo "<img width='$tSize' height='$tSize' border='2' alt='$curimg' src='./$curimg' />";
  echo "</a>";
  echo "</td>";
  echo "</tr>";		 

  echo "<tr>";	 # Name	 -----------------
  echo "<td>";		 
  echo "$curimg";
  echo "</td>";		 
  echo "</tr>";		 
  echo("</table>");
  # End of mini table --------------------------------------------  

  echo "</td>";

  $rowCount++;

}


if ( ($rowCount % $nCols) == 0){ 
   echo "</tr>";		 
   echo("</table>");
}


?>
</body>
</html>



<html>
 <head>
   <title>Most Recent Image</title>
   <meta http-equiv="refresh" content="300">
<style>

  

  table, th, td {
    border: 1px solid "#555655";
    border-spacing: 5px 5px;
    font-size: 90%;
 }

  body {
  font-family:Arial;
  font-color: "white";
 }
 img { border-color: black; }
</style>

</head>


<body bgcolor="#a4aaa5">

<?php 

/* FORMATTING */
$ncols = 6;
$curcol = 0;


/* SORT */
$files = array();
$dir = new DirectoryIterator('img');
foreach ($dir as $fileinfo) {
   $files[$fileinfo->getMTime()] = $fileinfo->getFilename();
}
   //krsort will sort in reverse order, which is what we want
krsort($files);

echo('<TABLE>');

$curCount = 0;  
foreach($files as $file)
{

   /* Check that it's not a thumbnail or usesless file */ 
   if ( strpos($file, 'M_th') == false &&  $file != "." && $file != "..")
   {

      if ($curcol == 0)
      {
            echo('<TR>');
      }

      $justTime = str_replace(".jpg","", $file);
      $justTime = str_replace("capture_","", $justTime);
      $justTime = str_replace("_"," ", $justTime);


      echo $justTime;
      echo "<br>";	         
      $tnfile = $file;
      $tnfile = str_replace("M.","M_th.",$tnfile);      
      $href = '<img border="1" width="780" height="480"  src="'."img/".$file.'" />';

      echo "<a href='" . "imgById.php?id=" . $curCount  . "'>$href</a>";

      echo('<H3>Raspberry Pi Window Camera</H3>');




      echo('</TD>');
      if ($curcol == $ncols){
            echo('</TR>');
      }
      $curcol = $curcol+1;
      if ($curcol == $ncols){
          $curcol = 0;
      }
      $prev = "img/".$file;
      $curCount++;
      break;
  }
}

  if ($curcol != $ncols){
           echo('</TR>');
   }
 	

 echo('</TABLE>');

?>



</body>

</html>

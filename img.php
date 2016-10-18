<html>
 <head>
   <title>Raspberry Pi Camera Contact Sheet</title>
   <meta http-equiv="refresh" content="300">
<style>
 table, th, td {
    border: 1px solid black;
    border-collapse:
    border-collapse: separate;
    border-spacing: 5px 5px;
    font-size: 90%;
 }

 body { font-family:Arial; }
 img { border-color: black; }
</style>

</head>


<body bgcolor="#FFF8DC">
<a href="index.html">Server Root</a><br>

  <H2>Raspberry Pi Window Camera</H2>

  <h4>Animated gif of yeserday</h4>
  <img src="yesterday.gif" alt="gif" border="1">
  <hr>
  <H3>Last 24 hours</H3>
   (click to enlarge)<br>
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
      echo('<TD bgcolor="#657383" align="center" >');
      
      $tnfile = $file;
      $tnfile = str_replace("M.","M_th.",$tnfile);      
      $href = '<img border="1"  src="'."img/".$tnfile.'" />';

      echo "<a href='" . "imgById.php?id=" . $curCount  . "'>$href</a>";

      echo "<br>";	   

      $justTime = str_replace(".jpg","", $file);
      $justTime = str_replace("capture_","", $justTime);

      echo $justTime;

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
  }
}

  if ($curcol != $ncols){
           echo('</TR>');
   }
 	

 echo('</TABLE>');

?>


</body>
</html>

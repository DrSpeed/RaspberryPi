
<html>
<html>
 <head>
   <title>Raspberry Pi Camera</title>
   <meta http-equiv="refresh" content="300">

<style>
 table, th, td {
    border: 1px solid black;
    border-collapse:
    border-collapse: separate;
    border-spacing: 5px 5px;
    font-size: 90%;
 }
 body {font-family:Arial;}
 img { border-color: black; }
</style>

</head>

<body bgcolor="#FFF8DC">
<h2>Raspberry Pi Camera Image</h2>

<?php 
echo "Return to <a href='img.php'>Index Page</a><p>";

/* SORT */
$files = array();
$dir = new DirectoryIterator('img');
foreach ($dir as $fileinfo) {
   $files[$fileinfo->getMTime()] = $fileinfo->getFilename();
}
//krsort will sort in reverse order, which is what we want
krsort($files);
   
/* Read url param */
$imgIndex = $_GET['id'];

echo('<TABLE>');
echo('<TR>');

$curCount = 0;
foreach($files as $file)
{
   /* Check that it's not a thumbnail or usesless file */ 
   if ( strpos($file, 'M_th') == false &&  $file != "." && $file != "..")
   {

      $tnfile = $file;
      $tnfile = str_replace("M.","M_th.",$tnfile);      
      $href = '<img border="1"  src="'."img/".$tnfile.'" />';

      $justTime = str_replace(".jpg","", $file);
      $justTime = str_replace("capture_","", $justTime);


      $later = $imgIndex - 1;
      if ($curCount == $later){
            echo('<TD bgcolor="#657383" align="center" >');
	    echo('<b>Later</b><br>');
	    echo "<a href='" . "imgById.php?id=" . $curCount  . "'>$href</a>";
	    echo('<br>' . $justTime);
	    echo('</TD>');
     }
      	 

      if ($curCount == $imgIndex){
      	 $imgFile = $file;
	 $imgTitle =  $justTime;
      } 

      $earlier = $imgIndex + 1;
      if ($curCount == $earlier){
            echo('<TD bgcolor="#657383" align="center" >');
	    echo('<b>Earlier</b><br>');
	    echo "<a href='" . "imgById.php?id=" . $curCount  . "'>$href</a>";
	    echo('<br>' . $justTime);
	    echo('</TD>');
      }

      $curCount++;
    }
}

echo('</TABLE>');

$href = '<img width="1024" height="770" border="1"  src="'."img/".$imgFile.'" />';
echo "<h4>" . $imgTitle . "</h4>";
echo "<a title='Click to enlarge'  href='" . "img/" . $imgFile . "'>$href</a>";

?>
</body>
</html>

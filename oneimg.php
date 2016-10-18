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

 body { font-family:Arial; } img { border-color: black; }
</style>

</head>


<body bgcolor="#FFF8DC">
Raspberry Pi Camera


<?php 

      $imgUrl = $_GET['imgUrl'];
      $prevImgUrl = $_GET['prev'];
      echo "prev  <a href='" . $prevImgUrl . "'>$prevImgUrl</a>";
      echo "current: <a href='" . $imgUrl . "'>$imgUrl</a>";
      echo "<br>";	   
    

?>

----------------
</body>
</html>

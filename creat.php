<?php
if(isset($_GET["tred"])&&isset($_GET["pyb"])){
	mkdir('ch/'.$_GET["tred"]);
	file_put_contents("ch/".$_GET["tred"]."/"."pub.txt", $_GET["pyb"]);
	echo "Ok!";
}  ?>
<?php
if(isset($_GET["tred"])&&isset($_GET["pub"])){
	mkdir('./ch/'.$_GET["tred"]);
	file_put_contents("./ch/".$_GET["tred"]."/"."pub.txt", $_GET["pub"]);
	echo "Ok!";
}  ?>
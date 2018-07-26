<?php
if(isset($_GET["name"])&&isset($_GET["pas"])&&isset($_GET["msg"])&&isset($_GET["pri"])){
	if(file_exists("./ch/".$_GET["name"]."/"."key.txt")==false&&file_exists("./ch/".$_GET["name"]."/"."lenta.txt")==false&&file_exists("./ch/".$_GET["name"]."/"."pas.txt")==false){
	mkdir('./ch/'.$_GET["name"]);
	file_put_contents("./ch/".$_GET["name"]."/"."key.txt", $_GET["pri"]);
	file_put_contents("./ch/".$_GET["name"]."/"."lenta.txt", $_GET["msg"]);
	file_put_contents("./ch/".$_GET["name"]."/"."pas.txt", hash("sha256",$_GET["pas"]));
	echo "Ok!";
}
else {
	echo "Huei";
}
}  ?>
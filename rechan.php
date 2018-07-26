<?php
if(isset($_GET["name"])&&isset($_GET["pas"])&&isset($_GET["msg"])){
	if(file_get_contents("./ch/".$_GET["name"]."/"."pas.txt")==hash("sha256",$_GET["pas"])){
		file_put_contents("./ch/".$_GET["name"]."/"."lenta.txt", $_GET["msg"]);
		echo "Ok!";
}
}  ?>
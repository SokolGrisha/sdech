<?php
if(isset($_GET["name"])&&isset($_GET["pas"])&&isset($_GET["msg"])){
	if(file_get_contents("./ch/".$_GET["name"]."/"."pas.txt")==hash("sha256",$_GET["pas"])){
		$fileopen=fopen("./ch/".$_GET["name"]."/"."lenta.txt", "a+");
		fwrite($fileopen,$_GET["msg"]);
		fclose($fileopen);
		echo "Ok!";
}
}  ?>
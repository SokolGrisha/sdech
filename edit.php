<?php
if(isset($_GET["tred"])&&isset($_GET["msg"])){
	file_put_contents("./ch/".$_GET["tred"]."/"."msg.txt", $_GET["msg"]);
	echo "Ok!";
}  ?>
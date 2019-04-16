<?php
	 function arrange()
	 {
	 	// This is the data you want to pass to Python
		$data = array('https://rensselaerdining.com/');

		$common_url = "./App/Common/Common/";

		// Execute the python script with the JSON data
//		$resultData = shell_exec("python3 " + $common_url + "test.py");
		exec("python3 App/Common/Common/test.py", $resultData);

		// Decode the result
//		$resultData = json_decode($result, true);

		// This will contain: array('status' => 'Yes!')
		var_dump($resultData);
		var_dump();
		return $resultData;
	 }
<?php
	 function arrange($tmp,$str)
	 {
	 	// This is the data you want to pass to Python
		$data = array('https://rensselaerdining.com/');

		// Execute the python script with the JSON data
		$result = shell_exec('python ./data_fetch.py ' . escapeshellarg(json_encode($data)));

		// Decode the result
		$resultData = json_decode($result, true);

		// This will contain: array('status' => 'Yes!')
		return $resultData;
		
	 }
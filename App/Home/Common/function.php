<?php
	// function arrange($tmp,$str)
	// {
	// 	$sub = array();
	// 	for ($i=0; $i < count($tmp); $i++) { 
	// 		array_push($sub, $tmp[$i][$str]);
	// 	}
	// 	return array($str => $sub);

	// }

	// function mergePoster($tmp,$array)
	// {

	// 	$poster = array();
	// 	for ($i=0; $i < count($array); $i++) {
	// 		$poster = array_merge($poster,arrange($tmp,$array[$i]));
	// 	}
	// 	return $poster;
	// }

	// function arrangePage($poster,$ppp)
	// {
	// 	$page = array(
	// 		'dataCount' => count($poster),
	// 		'ppp' => $ppp,
	// 		'pageCount' => (int)(count($poster)/$ppp)+1,
	// 		);
	// 	return $page;
	// }

	function getPage($table,$eachNum,$where)
	{
		$count = $table->where($where)->count();
		$page = new \Think\Page($count,$eachNum);
		
		$page->setConfig('prev','prev');
    	$page->setConfig('next','next');
    	$page->setConfig('last','last');
    	$page->setConfig('first','first');
    	$page->setConfig('theme','%FIRST% %UP_PAGE% %LINK_PAGE% %DOWN_PAGE% %END%');

    	return $page;

	}

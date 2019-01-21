<?php
namespace Home\Model;
use Think\Model;
Class MessagerModel extends Model
{
	protected $_validate = array(
		//default
		// array('title' ,'require' ,'Title is required!')
		);
	public function cposter($data)
	{
		$title = $data['title'];
		
	}

}
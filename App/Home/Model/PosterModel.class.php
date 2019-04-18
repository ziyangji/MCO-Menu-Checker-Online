<?php
namespace Home\Model;
use Think\Model;
Class PosterModel extends Model
{
	protected $_validate = array(
		//default
		array('title' ,'require' ,'Title is required!')
		);
	public function cposter($data)
	{
		$title = $data['title'];
		
	}

	public function getPosters()
	{
		$posters = $this->order('posterId DESC')->select();
		return $posters;
	}


		

}
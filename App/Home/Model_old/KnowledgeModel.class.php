<?php
namespace Home\Model;
use Think\Model;
Class KnowledgeModel extends Model
{
	protected $_validate = array(
		//default
		// array('title' ,'require' ,'Title is required!')
		);
	public function getCourse($section)
	{
		return $this->where("section='$section'")->select();
	}
}
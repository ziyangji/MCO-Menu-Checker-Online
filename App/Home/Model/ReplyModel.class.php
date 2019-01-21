<?php
namespace Home\Model;
use Think\Model;
Class ReplyModel extends Model
{
	protected $_validate = array();

	public function getReplies($posterId)
	{
		$replies = $this->where("posterId = '$posterId'")->order('cdate')->select();
		return $replies;
	}

		

}
<?php
namespace Home\Controller;
use Think\Controller;
class CommonController extends Controller
{
	public function _initialize()
	{
		header('Content-Type:text/html;charset=utf-8');
		if( !session('uid') ) {
//			TODO: prevent user data leaking
//			$this->redirect("Admin/Login/login");
//			exit;
		}
	}
	
	
}
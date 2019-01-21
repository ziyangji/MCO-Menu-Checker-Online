<?php
namespace Home\Controller;
use Think\Controller;
class CommonController extends Controller
{
	public function _initialize()
	{
		header('Content-Type:text/html;charset=utf-8');
	}

	public function logout()
	{
		session('name',null);
		$this->redirect('Index/index',array(),0,'');
	}
}
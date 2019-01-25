<?php
namespace Home\Controller;
use Think\Controller;
class HomeController extends CommonController
{
	public function index()
	{
		
		$this->assign('name', session('name'));
		$this->display();
	}

	public function messager()
	{
		$messager = D('Messager');
		//subpage
		$page = getPage($messager,5,"messagerId>0");
		$list = $messager->field(true)->order('messagerId DESC')->limit($page->firstRow.','.$page->listRows)->select();

		$this -> assign('page',$page->show());
		$this -> assign('list',$list);

		$this->assign('name', session('name'));
		$this->display();
	}
}
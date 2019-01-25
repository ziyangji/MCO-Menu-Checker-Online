<?php
namespace Home\Controller;
use Think\Controller;
class AdminController extends CommonController
{
	public function index()
	{
		$user = D('User');
		$friend = D('Friend');

		$name = I('session.name');
		$age = $user->where("name = '$name'")->find()['age'];
		$email = $user->where("name = '$name'")->find()['email'];

		$userThumb;

		$friend = D('Friend');
		$page = getPage($friend,5,"id>0");
		$list = $friend->field(true)->order('id DESC')->limit($page->firstRow.','.$page->listRows)->select();

		$this -> assign('page',$page->show());
		$this -> assign('list',$list);

		$admin = array(
			'name' => $name,
			'age' => $age,
			'email' => $email
			);

		$this->assign('admin', $admin);
		$this->display();
	}

	public function changeProfile()
	{
		$post = I('post.');
		$name = session('name');
		$user = D('User');
		switch ($post['pk']) {
			case '1':
				//name
				// $data['name'] = $post['value'];
				// $user->where("name='$name'")->save($data);
				break;
			case '2':
				//age
				$data['age'] = $post['value'];
				$user->where("name='$name'")->save($data);
				break;
			case '3':
				//email
				$data['email'] = $post['value'];
				$user->where("name='$name'")->save($data);
				break;
			default:

				break;
		}
		
		exit();
	}
}
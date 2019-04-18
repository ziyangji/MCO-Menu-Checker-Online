<?php
namespace Home\Controller;
use Think\Controller;
class ForumController extends CommonController
{
	public function index()
	{

		$poster = D('Poster');
		//subpage
		$page = getPage($poster,5,"posterId>0");
		$list = $poster->field(true)->order('posterId DESC')->limit($page->firstRow.','.$page->listRows)->select();

		$this -> assign('page',$page->show());
		$this -> assign('list',$list);

		$this->assign('name', session('name'));
		$this->display();

	}


	public function page($posterId)
	{

		session('posterId',$posterId);
		$user = D('User');
		$poster = D('Poster');
		$reply = D('Reply');

		$getReply = $reply;


		//subpage
		$page = getPage($getReply,5,"posterId = '$posterId'");
		$list = $reply->field(true)->where("posterId = '$posterId'")->order('cdate')->limit($page->firstRow.','.$page->listRows)->select();
		$this -> assign('page',$page->show());
		$this -> assign('list',$list);
		$this->assign('users', $user->listUsers());
		$this->assign('name', session('name'));
		$this->display();
	}

	public function search()
	{
		$key = I('post.')['searchKey'];
		$poster = D('Poster');
		$where['title'] = array('like', "%$key%" );
		$page = getPage($poster,5,$where);
		$list = $poster->field(true)->where($where)->order('posterId DESC')->limit($page->firstRow.','.$page->listRows)->select();


		$this -> assign('page',$page->show());
		$this -> assign('list',$list);

		$this->assign('name', session('name'));
		$this->display();
	}

	public function createPage()
	{
		$info = I("post.");
		$userId = D('User')->getId(session('name'));

		$new_poster = array(
			"userId" => $userId,
            "title" => $info["title"],
            "name" => session('name'),
           	"cdate" => date("Y-m-d H:i:s",time())
        );

		$poster = D('Poster');
		if (!$poster->create($new_poster)) {
			$this->error($poster->getError());
		} else{
			if($posterId = $poster->add($new_poster)){

        	}else{
        	  	$this->error("Failure!");
        	}
		}

		$add_reply = array(
            "posterId" => $posterId,
			"userId" => $userId,
            "name" => session('name'), 
            "content" => $info["content"],
           	"cdate" => date("Y-m-d H:i:s",time())
        );
		$reply = D('Reply');
		if (!$reply->create($new_poster)) {
			$this->error($reply->getError());
		} else{
			if($replyId = $reply->add($add_reply)){

        	}else{
        	  	$this->error("Failure!");
        	}
		}

        $this->ajaxReturn();
        exit();
	}

	public function createReply()
	{
		$info = I("post.");
		$userId = D('User')->getId(session('name'));

		$poster = D('Poster');

		$add_reply = array(
            "posterId" => session('posterId'),
			"userId" => $userId,
            "name" => session('name'), 
            "content" => $info["content"],
           	"cdate" => date("Y-m-d H:i:s",time())
        );
		$reply = D('Reply');
		if (!$reply->create($new_poster)) {
			$this->error($reply->getError());
		} else{
			if($replyId = $reply->add($add_reply)){

        	}else{
        	  	$this->error("Failure!");
        	}
		}

        // $this->ajaxReturn();
        exit();
	}

	public function deleteReply($replyId)
	{
		$reply = D('Reply');
		$reply->where("replyId = '$replyId'")->delete();
		exit();
	}

	public function deletePoster($posterId)
	{
		$poster = D('Poster');
		$poster->where("posterId = '$posterId'")->delete();
		var_dump($poster->where("posterId = '$posterId'")->find());
		exit();
	}
}
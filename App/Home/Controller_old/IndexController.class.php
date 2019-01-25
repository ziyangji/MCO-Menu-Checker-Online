<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends CommonController
{
    public function index()
    {
       	if (session('?name')) {
       		$this->success('Loading...', U('Admin/index'));
       	} else {
       		$this->display();
       	}
       	
        
    }
    
    public function signIn()
    {
      $info = I("post.","","htmlspecialchars");
      $data = array(
            "name" => $info['name'],
            "password"=> $info['password']
        );

      $user = D('User');

      $result = $user->checkSignIn($data);

    	if(!$user->create($data,4)){
        $this->error($user->getError());
      } else {        
        if ($result) {
          session('name', $data['name']);
          $this->success('Sign In successfully. Loading...', U('Admin/index'));
        } else {
          $this->error('Incorrect Name or Password!');
        }
        
		  }
        // $this->display();
    }

    public function signUp()
    {
    	  $info = I("post.","","htmlspecialchars");
        $data = array(
            "name" => $info['n_name'],
            "email" => $info['n_email'],
            "password"=> $info['n_password']
        );
        
        $user = D("User");
        
        if(!$user->create($data, 1)){
          $this->error($user->getError());
        }
        $data = array(
              "name" => $info['n_name'],
              "email" => $info['n_email'],
              "password"=> $info['n_password'],
              'permission' => 1, 
              'cdate' => date("Y-m-d H:i:s",time())
              );
        if($user->add($data)){
          session('name', $data['name']);
          $this->success("Sign up successfullly. Loading...", U('Admin/index'));
        }else{
          $this->error("failure!");
        }
    	// $this->display();
    }
}
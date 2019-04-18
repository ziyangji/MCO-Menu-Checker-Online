<?php
namespace Home\Model;
use Think\Model;
Class UserModel extends Model
{
	protected $_validate = array(
		//default
		array('name' ,'require' ,'Please Enter Username!'),
		array('password' ,'require' ,'Please Enter Password!'),
		array('email' ,'email' ,'email address is not availible'),
		//signup
		array('name' ,'' ,'Account has already existed!' ,0 ,'unique' ,1)
		//signin 4
		);
	public function checkSignIn($data)
	{
		$name = $data['name'];
		$password = $data['password'];
		$result = $this->where("name='$name' and password='$password'")->find();

		if($result){
			return true; 
			
		}else{
			return false;
		}
		
	}

	public function getId($name)
	{
		$result = $this->where("name='$name'")->find();
		return $result['id'];
	}

	public function listUsers()
	{
		$result = $this->select();
		return $result;
	}
}

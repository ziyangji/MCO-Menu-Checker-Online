<?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends CommonController
{
    public function index()
    {
        $this->redirect('Index/home');
        $content = array(
            0 => 'Menu Checker',
            1 => '\tAn online preview of the RPI dining hall menus.\n\tStudents and dinning hall staffs will be able to upload both text descriptions and pictures of dishes provided by each of the dinning halls.\n\tThe menus will be updated "mealy" by users, and we are considering to collaborate with the dinning halls to make it easier.'
        );
        
        $this->assign('content', $content);

        $this->assign('hh', arrange());

        $this->display();
    }
    
    public function home()
    {
        
        $dininghall = array(
            0 => array(
                'id' => 'cms',
                'name' => "Commons Dining Hall",
                'addr' => "TBD"
            ),
            1 => array(
                'id' => 'barh',
                
                'name' => "Barh Dining Hall",
                'addr' => "100 Albright Ct"
            ),
            2 => array(
                'id' => 'sage',
                'name' => "Sage Dining Hall",
                'addr' => "P8HC+WP"
            ),
            3 => array(
                'id' => 'blm',
                'name' => "Sage Dining Hall",
                'addr' => "1800 6th Ave"
            ),
        );

        $this->assign('data', $dininghall);
        
        $this->display();
    }
    
    public function restaurant()
    {
        $res_name = I('get.name');
        $this->assign('name', $res_name);
        $this->display();
    }
}
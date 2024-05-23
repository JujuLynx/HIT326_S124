<?php  
    class Controller_Example extends Controller { 
        public function before() {
            echo "This message comes from <em>before()</em> method</br>"; 
        }

        public function action_home() { 
            echo "FuelPHP-Employee application!"; 
        }
        public function action_index() { 
            echo "This is the index method of employee controller"; 
        }
        public function action_show() { 
            echo "This is the show method of employee controller"; 
        }

        public function after($response) { 
            if ( ! $response instanceof Response) { 
                $response = \Response::forge($response, $this->response_status); 
            }
            return $response; 
        }
    }
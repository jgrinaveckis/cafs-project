<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Requests\LoginRequest;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function show() {
        return view('home');
    }

    public function login(LoginRequest $request) {

        $creds = request(['email', 'password']);

        if(!Auth::validate($creds)):
            return redirect('/')->with('error', "User cant be authorised");
        endif;
        
        #retrieve user
        $user = Auth::getProvider()->retrievedByCredentials($creds);
        Auth::login($user);

        return $this->userAuthenticated($request, $user);
    }

    protected function userAuthenticated(Request $request, $user) {
        return redirect()->to(route('auth.map'));
    }
}

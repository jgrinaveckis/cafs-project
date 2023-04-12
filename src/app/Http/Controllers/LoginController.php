<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Requests\LoginRequest;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function show() {
        return view('auth.login');
    }

    public function login(LoginRequest $request) {
        $creds = $request->getCreds();

        if(!Auth::validate($creds)):
            return redirect()->to('login')->withErrors(trans('auth.failed'));
        endif;

        $user = Auth::getProvider()->retrievedByCredentials($creds);
        Auth::login($user);

        return $this->userAuthenticated($request, $user);
    }

    protected function userAuthenticated(Request $request, $user) {
        return redirect()->intended();
    }
}

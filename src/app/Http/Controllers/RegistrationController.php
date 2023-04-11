<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use App\Http\Requests\RegistrationRequest;

class RegistrationController extends Controller
{

    public function show() {

        return view('register');
    }

    public function register(RegistrationRequest $request) {
        
        $user = User::create($request->validated());
        auth()->login($user);
        return redirect('/')->with('success', "User was registered!");
    }
}

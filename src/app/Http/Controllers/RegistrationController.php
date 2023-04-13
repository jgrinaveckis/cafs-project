<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use App\Http\Requests\RegistrationRequest;
use Illuminate\Support\Facades\Hash;

class RegistrationController extends Controller
{

    public function show() {

        return view('register');
    }

    public function register(RegistrationRequest $request) {

        return redirect('/')->with('success', "User was registered!");
    }
}

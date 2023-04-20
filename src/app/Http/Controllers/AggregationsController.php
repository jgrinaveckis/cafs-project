<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Gate;

class AggregationsController extends Controller
{
    public function show() {
        return response(["success", "User authorized"], 200);
    }
}

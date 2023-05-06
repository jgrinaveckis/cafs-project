<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\LoginController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\RegistrationController;
use App\Http\Controllers\LeadController;
use App\Http\Middleware\Authenticate;
use App\Http\Middleware\AdminMiddleware;
use App\Http\Middleware\CorsMiddleware;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::post('/login', [LoginController::class, 'login']);
Route::post('/register', [RegistrationController::class, 'register']);

Route::middleware([
    'auth'
])->group(function () {
    Route::get('/auth/user', [AuthController::class, 'info']);
    Route::middleware([
        AdminMiddleware::class,
        CorsMiddleware::class
    ])->group(function () {
        Route::get('/leads/bycountry', [LeadController::class, 'getCountByCountry']);
        Route::get('/leads/bystate', [LeadController::class, 'getCountByState']);
        Route::post('/test/insert', [LeadController::class, 'insert']);
    });
});
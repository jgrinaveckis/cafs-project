<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\LoginController;
use App\Http\Controllers\LogoutController;
use App\Http\Controllers\MapController;
use App\Http\Controllers\RegistrationController;
use App\Http\Controllers\ConsumerController;

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

Route::middleware(['auth'])->group(function () {
    Route::post('/logout', [LogoutController::class, 'logout']);
    Route::middleware(['admin'])->group(function () {
        Route::get('/aggregations', [AggregationsController::class, 'show']);
    });

});
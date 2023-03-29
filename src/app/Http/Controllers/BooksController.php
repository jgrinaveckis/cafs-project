<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BooksController extends Controller
{    
    public function list() {
        return "This lists all books!";
    }

    public function get(string $id) {
        return `This lists one, ${id}, book!`;
    }

    public function create(string $id) {
        return `This create one, ${id}, book!`;
    }

    public function delete() {
        return "This deletes all books!";
    }

    public function update(string $id) {
        return `This updates one, ${id}, book!`;
    }
}
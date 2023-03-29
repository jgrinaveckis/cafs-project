<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Task;

class TaskController extends Controller
{
    public function list()
    {
        $tasks = Task::all();
        return $tasks;
    }

    public function find($id)
    {
        $task = Task::find($id);
        return $task;
    }

    public function create(Request $request)
    {
        $input = $request->all();

        Task::create($input);
    }

    public function update($id, Request $request)
    {
        $task = Task::find($id);
        $fieldsToUpdate = $request->all();
        $task->title = $fieldsToUpdate['title'];
        $task->deadline = $fieldsToUpdate['deadline'];
        $task->save();

        // Task::where('id', $id)
        //     ->update([
        //         'title' => $fieldsToUpdate['title'],
        //         'deadline' => $fieldsToUpdate['deadline']
        //     ]);
    }
}

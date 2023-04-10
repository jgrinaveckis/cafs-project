<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Contracts\Validation\Factory as ValidationFactory;

class LoginRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\Rule|array|string>
     */
    public function rules(): array
    {
        return [
            'username' => 'required',
            'password' => 'required'
        ];
    }

    public function getCreds() {

        $username = $this->get('username');
        if($this->isEmail($username)) {
            return [
                'email' => $username,
                'password' => $this->get('password')
            ]
        }
        return $this->only('username', 'password');
    }

    protected function isEmail($field) {
        //think if actually this validation and username stuff is needed at all
        $validator = $this->container->make(ValidationFactory::class);
        return ! $validator->make(
            ['username' => $field],['username' => 'email']
        )->fails();
    }
}

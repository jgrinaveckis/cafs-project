<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Junges\Kafka\Facades\Kafka;
use Junges\Kafka\Contracts\KafkaConsumerMessage;

class ConsumeMessages extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'kafka:consume {topic}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = "Consume Kafka messages from 'topic'.";

    public function createConsumer($topic) {
        return Kafka::createConsumer()->subscribe([$topic]);
    }
    /**
     * Execute the console command.
     */
    public function handle(): void
    {
        $topic = $this->argument('topic');
        $consumer = createConsumer($topic);

        $consumer->withAutoCommit()
        ->withHandler(function(KafkaConsumeMessage $message) {
            $msgBody = $message->getBody();
            var_dump(json_decode($msgBody, true));
           })
           ->build();

        $consumer->consume();
    }
}

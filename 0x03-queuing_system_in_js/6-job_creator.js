import kue from 'kue';

const queue = kue.createQueue();

const job = {
  phoneNumber: 'string',
  message: 'string',
};

const pushCode = queue.create('push_notification_code', job).save((err) => {
  console.log(`Notification job created: ${pushCode.id}`);
});

ls.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});

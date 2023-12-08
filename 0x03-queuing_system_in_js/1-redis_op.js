import { createClient } from 'redis';
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error.message);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, response) => {
    redis.print(`Reply: ${response}`);
  });
}

async function displaySchoolValue(schoolName) {
  try {
    const result = await promisifiedGet(schoolName);
    redis.print(result);
  } catch (error) {
    redis.print(error.message);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

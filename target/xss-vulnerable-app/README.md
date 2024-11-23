# XSS Vulnerable React application

> This is a Basic React Web application
>
> [Github Repository](https://github.com/desmigor/xss-vulnerable-app)

## 0. Deployment instructions with the docker image

To build and tag the docker image, use:
```
docker build -t webapp .
```
To start the container once the build is done, use:
```
docker run \
    -it \
    --rm \
    -v ${PWD}:/app \
    -v /app/node_modules \
    -p 3000:3000 \
    -e CHOKIDAR_USEPOLLING=true \
    webapp
```
The app will be exposed on http://localhost:3000

## 1. Vulnerability Description
Cross-site scripting, often abbreviated as XSS, is a type of attack in which malicious scripts are injected into websites and web applications for the purpose of running on the end user's device. During this process, unsanitized or unvalidated inputs (user-entered data) are used to change outputs.
## 2. Technical description based on my code
The main app logic resides in [App.jsx]() file. Basically, the there're two fields in the app.
- Name inputfield.
- Message textarea.

![user-interface](https://github.com/desmigor/xss-vulnerable-app/blob/main/screenshots/user-interface.png)

The message input is printed bellow the form after clicking the "Submit" button. The way the input is printed, it is injected as <u>Raw HTML</u> into the page or evaluate their input as JavaScript code using an empty DIV. Reference to the code below.

```
<div ref={divRef} className='notifyWrapper'>
</div>
```

## 3. Exploitation Process with screenshot

As explained above, in this case; any code can be injected in the <u> message text area </u>field and can be exploited. For example, for testing, I used this code to show the example of a script that can be runned. Eventhough this seems to be an easy code, can be advanced and cause more problems.

```
<img onError=alert('Hacked.') src='invalid.url.com'>
```
![bad-code](https://github.com/desmigor/xss-vulnerable-app/blob/main/screenshots/bad-code.png)

## 4. Fixing Code

The best way to fix this problem, is to use a variable and using in-built <u>append()</u> function instead of printing Raw text. Here is the full code to fix the problem. This will print the input as a variable in string type instead of running it as a code.

```
<div id='validation' className='notifyWrapper'>
{validateMessage}
</div>
```

![fixed-code](https://github.com/desmigor/xss-vulnerable-app/blob/main/screenshots/fixed-code.png)

```
function App() {
  const [value, setValue] = React.useState("");
  const validateMessage = async () => {
    const validationElement = document.getElementById('validation');
    const validationMessage = value
    validationElement.append(validationMessage);
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>XSS Vulnerability</h1>
        <p>by Igor Mpore</p>
      </header>
      <div className='formWrapper'>
        <div className='form'>
          <input type="text" placeholder='Your name' />
          <textarea value={value} onChange={(e) => setValue(e.target.value)} placeholder='Type your Print Message'></textarea>
          <button onClick={validateMessage}>Submit</button>
        </div>
      </div>
      <div id='validation' className='notifyWrapper'>
        {validateMessage}
      </div>
    </div>
  );
}
```

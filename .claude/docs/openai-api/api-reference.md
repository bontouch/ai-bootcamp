# OpenAI Responses API

The **Responses API** allows you to create, retrieve, delete, and manage model responses.
It supports text, image, file inputs, reasoning models, and built-in or custom tools.

---

## Endpoints

### 1. Create a Model Response

**POST**
`https://api.openai.com/v1/responses`

Creates a model response. You can provide **text, image, or file inputs** and configure output.

#### Request Body Parameters

* **background** (boolean, default: `false`)
  Run response in the background.
* **conversation** (string | object, default: `null`)
  Links response to a conversation.
* **include** (array | null)
  Specify additional output data to include. Supported values:

  * `code_interpreter_call.outputs`
  * `computer_call_output.output.image_url`
  * `file_search_call.results`
  * `message.input_image.image_url`
  * `message.output_text.logprobs`
  * `reasoning.encrypted_content`
* **input** (string | array)
  Input data (text, images, or files).
* **instructions** (string | null)
  System/developer message inserted into model context.
* **max\_output\_tokens** (int | null)
  Token limit for generated response.
* **max\_tool\_calls** (int | null)
  Maximum number of tool calls allowed.
* **metadata** (map)
  Up to 16 key-value pairs (string: max 64 chars, value: max 512 chars).
* **model** (string, required)
  Model ID (e.g., `gpt-4o`, `o3`).
* **parallel\_tool\_calls** (boolean, default: `true`)
  Allow parallel tool execution.
* **previous\_response\_id** (string | null)
  Chain to previous response.
* **prompt** (object | null)
  Reference to a prompt template.
* **prompt\_cache\_key** (string)
  For caching optimizations.
* **reasoning** (object | null, for `gpt-5` and `o-series`)
  Options for reasoning models.
* **safety\_identifier** (string)
  Stable hashed user identifier for policy enforcement.
* **service\_tier** (string | null, default: `auto`)
  Processing type: `auto`, `default`, `flex`, `priority`.
* **store** (boolean, default: `true`)
  Whether to store the response for retrieval.
* **stream** (boolean, default: `false`)
  Stream output via SSE.
* **stream\_options** (object | null)
  Options for streaming.
* **temperature** (number, default: `1`)
  Sampling temperature (0–2).
* **text** (object)
  Options for text/structured outputs.
* **tool\_choice** (string | object)
  Tool selection strategy.
* **tools** (array)
  Built-in or custom tools available.
* **top\_logprobs** (int, 0–20)
  Number of top logprobs to return.
* **top\_p** (number, default: `1`)
  Nucleus sampling parameter.
* **truncation** (string, default: `disabled`)
  Strategy: `auto` or `disabled`.
* **user** (string, deprecated)
  Use `safety_identifier` instead.

#### Example Request

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
```

---

### 2. Get a Model Response

**GET**
`https://api.openai.com/v1/responses/{response_id}`

Retrieves a model response by ID.

#### Path Parameters

* **response\_id** (string, required)

#### Query Parameters

* **include** (array)
* **include\_obfuscation** (boolean, default: `true`)
* **starting\_after** (integer)
* **stream** (boolean)

#### Example

```python
response = client.responses.retrieve("resp_123")
print(response)
```

---

### 3. Delete a Model Response

**DELETE**
`https://api.openai.com/v1/responses/{response_id}`

Deletes a model response by ID.

#### Example

```python
response = client.responses.delete("resp_123")
print(response)
```

---

### 4. Cancel a Model Response

**POST**
`https://api.openai.com/v1/responses/{response_id}/cancel`

Cancels a background response.

#### Example

```python
response = client.responses.cancel("resp_123")
print(response)
```

---

### 5. List Input Items

**GET**
`https://api.openai.com/v1/responses/{response_id}/input_items`

Returns input items for a given response.

#### Query Parameters

* **after** (string)
* **include** (array)
* **limit** (int, default: 20, range: 1–100)
* **order** (string: `asc` or `desc`)

#### Example

```python
response = client.responses.input_items.list("resp_123")
print(response.data)
```

---

## Response Object

Example structure returned by API:

```json
{
  "id": "resp_67ccd3a9da748190baa7f1570fe91ac6",
  "object": "response",
  "created_at": 1741476777,
  "status": "completed",
  "model": "gpt-4o-2024-08-06",
  "output": [
    {
      "type": "message",
      "role": "assistant",
      "content": [
        { "type": "output_text", "text": "Sample response text." }
      ]
    }
  ],
  "usage": {
    "input_tokens": 328,
    "output_tokens": 52,
    "total_tokens": 380
  },
  "temperature": 1,
  "store": true,
  "parallel_tool_calls": true
}
```

---

## Input Item List Example

```json
{
  "object": "list",
  "data": [
    {
      "id": "msg_abc123",
      "type": "message",
      "role": "user",
      "content": [
        { "type": "input_text", "text": "Tell me a bedtime story." }
      ]
    }
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc123",
  "has_more": false
}
```

---

## Supported Features

* ✅ Text inputs/outputs
* ✅ Image inputs
* ✅ File inputs
* ✅ Streaming responses
* ✅ Tool calls (built-in & custom)
* ✅ Reasoning models (`gpt-5`, `o-series`)

---

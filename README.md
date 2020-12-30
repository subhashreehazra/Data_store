# Data_store

**THE PROBLEM STATEMENT**

Build the file based key value data store that supports the basic CRD(create, read and delete) operations. The data store is meant to be used as a local storage for one single person on one laptop. The data store must be exposed as a library to clients that can  instatantiate a class and work with the data store.

The data store will support the **following requirements**

  - It can be initialized using an optional file path. If one is not provided, It will reliably create itself in a reasonable location on the laptop.
  - A new key-value pair cab be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object -  capped at 16KB.
  - If Create is invoked for an existing key, an appropriate error must be returned.
  - A Read opertion on a key can be performed by providing the key, and recieving the value in response, a JSON object.
  - A Delete operation can be performed by providing the key.
  - Every key supports setting a Time-to-live property when it is created. The property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-to-live proeprty has been expired , the key will no longer be available for read or delete operations.
  - Appropriate error responses must always be returned to the client if it uses the data store in unexpected ways or breaches any limits.

The data store will also support the following **non-functional requirements**
  - The size of the file storing data must never exceed 1GB.
  - More than one client process cannot be allowed to use the same file as a data store at any given time.
  - A client process is allowed to access the data using multiple threads, if it desires to. The data store must therefore be thread safe.
  - The client will bear as little memory  costs as possible to use the data store, while deriving maximum performance with respect to the response times for accessing the data store.
  
  **OUTPUT**
  !https://github.com/subhashreehazra/Data_store/blob/main/output.png


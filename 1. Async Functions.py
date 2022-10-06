
# ///////////////////////
# //  Async Functions  //
# ///////////////////////
import asyncio

# // Unlike regular functions, asynchronous functions need to
# // be awaited.
# //
# // This works as shown below

async def main():
    # // Await the function
    await test_function()


# // Async function
async def test_function():
    print("test function called!")


# // Although to call an async function outside of another
# // async function you need to use the asyncio library.
# // Example:

# // This gives us an error
await main()


# // Therefore we must use...
asyncio.run(main())
# // Which will run the main function 
# // without giving us any errors

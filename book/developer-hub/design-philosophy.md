# Design Philosophy

Project Elära's software should be robust, easily maintainable, and simple - requirements essential to building software that lasts for generation upon generation. Therefore, we insist on the following principles for software development:

1. Each library (or software) is intended to do one thing well. Instead of overloading existing software with more features, make new software instead.

2. Keep the (dependency-excluded) codebase of software under 10K lines of code, and preferably under 5K lines of code.

3. Use only the project's own libraries as dependencies when possible, and minimize use of dependencies

4. Keep everything licensed under public domain, as with the rest of Project Elära

The reason for the first principle is that software that has too many features easily becomes unmaintainable. More features means more complexity, which means a more difficult-to-understand codebase, which restricts work on a codebase to those who are already familiar with the software. We want everyone to be able to contribute, so we want to avoid that as possible. The reasoning is similar withe second rule. We want software that can be modified for generations, so we need the codebase to be manageably small.

The reason for the third principle is also similar - dependencies lead to more complexity, and to more code that could lead to bugs. In general, fewer code leads to fewer bugs, which leads to more maintainable software. The use of the project's own libraries is intended to protect the independence of the project from dependency interference. Finally, the public domain licensing is needed to keep the software always free and available to everyone.

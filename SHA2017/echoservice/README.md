# echoservice

## Description

This is a format string vulnerability in Objective-C. We abuse
the "%@" placeholder to trigger a function call using a fake
object struct crafted on the heap.

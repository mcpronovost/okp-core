export function onRequest (context, next) {
    try {
        let protocol = context.url.protocol
        let ip = context.clientAddress
        context.locals.ip = `${protocol}//${ip.split(":").pop()}:8000`
        context.locals.apiwagtail = `${protocol}//${ip.split(":").pop()}:8000/api-wagtail`
    } catch {
        context.locals.ip = ""
        context.locals.apiwagtail = ""
    }
    return next()
};
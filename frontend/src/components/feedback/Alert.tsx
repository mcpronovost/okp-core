import { useState } from "react";
import classNames from "classnames";
import {
  CircleAlert,
  CircleCheck,
  TriangleAlert,
  Info,
  CircleX,
  X,
} from "lucide-react";
import { AlertProps, AlertVariantType, AlertIconNameType } from "@/types";

const ICON_MAP: Record<
  Exclude<
    AlertVariantType,
    "tier0" | "tier1" | "tier2" | "tier3" | "tier4" | "tier5" | "tier6"
  >,
  JSX.Element
> = {
  success: <CircleCheck />,
  error: <CircleX />,
  warning: <TriangleAlert />,
  info: <Info />,
  default: <CircleAlert />,
};

const STRING_ICON_MAP: Record<AlertIconNameType, JSX.Element> = {
  CircleCheck: <CircleCheck />,
  CircleX: <CircleX />,
  TriangleAlert: <TriangleAlert />,
  Info: <Info />,
  CircleAlert: <CircleAlert />,
};

export default function OkpAlert({
  variant = "default",
  icon = true,
  closable = false,
  onClose,
  title,
  message,
  children,
}: AlertProps) {
  const [isVisible, setIsVisible] = useState(true);

  const getIconElement = () => {
    if (icon === true) return ICON_MAP[variant] || <CircleAlert />;
    if (typeof icon === "string" && icon in STRING_ICON_MAP)
      return STRING_ICON_MAP[icon as AlertIconNameType];
    return null;
  };

  const handleClose = () => {
    setIsVisible(false);
    onClose?.();
  };

  if (!isVisible) return null;

  return (
    <div className={classNames("okp-alert", `okp-alert-variant-${variant}`)}>
      {icon && <div className="okp-alert-icon">{getIconElement()}</div>}
      <div className="okp-alert-content">
        {title && <p className="okp-alert-content-title">{title}</p>}
        {message && <p className="okp-alert-content-message">{message}</p>}
        {children}
      </div>
      {closable && (
        <div className="okp-alert-close" onClick={handleClose}>
          <X />
        </div>
      )}
    </div>
  );
}

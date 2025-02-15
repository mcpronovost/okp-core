export type AlertVariantType =
  | "success"
  | "error"
  | "warning"
  | "info"
  | "default"
  | "tier0"
  | "tier1"
  | "tier2"
  | "tier3"
  | "tier4"
  | "tier5"
  | "tier6";

export type AlertIconNameType =
  | "CircleCheck"
  | "CircleX"
  | "TriangleAlert"
  | "Info"
  | "CircleAlert";

export interface AlertProps {
  variant?: AlertVariantType;
  icon?: AlertIconNameType | boolean;
  closable?: boolean;
  title?: string;
  message?: string;
  children?: React.ReactNode;
  onClose?: () => void;
}

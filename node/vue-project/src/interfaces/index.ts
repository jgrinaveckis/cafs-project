export type ILead = {
    ip: string,
    iso_state: string,
    iso_country: string,
    created_at: Date
}

export type IUser = {
    id: number
    name: string
    email: string
    role: Role
    created_at: string | null
    updated_at: string | null
  }

export enum Role {
    admin = 'admin',
    regular = 'regular'
  }